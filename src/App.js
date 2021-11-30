import "./App.css"
import { useEffect, useState } from "react"
import Section from "./components/Section"
import HeroSection from "./components/HeroSection"
import NavBar from "./components/NavBar"

const App = () => {
  const pageSize = 4
  const [requestedPage, setRequestedPage] = useState(0)
  const [pageState, setPageState] = useState(null)
  const [genres, setGenres] = useState(null)
  const [isFetching, setIsFetching] = useState(false)

  const fetchData = async () => {
    if (! isFetching)  {
      setIsFetching(true)
      const response = await fetch("/.netlify/functions/getGenres", {
        method: "POST",
        body: JSON.stringify({pageState, pageSize}),
      })
      const responseBody = await response.json()
      setPageState(responseBody.data.reference_list.pageState)
      setGenres(gs => (gs || []).concat(responseBody.data.reference_list.values))
      setIsFetching(false)
    }
  }

  useEffect(() => {
    // we trigger the first page of genres at the beginning
    setRequestedPage(1)
  }, [])

  useEffect(() => {
    const goalItems = pageSize * requestedPage
    const currentItems = (genres || []).length
    const bottomReached = currentItems > 0 && pageState === null
    // we ask for more genres if we are not at bottom of infinite scroll
    // (and if there are less items than the nominally requested pages)
    if ((goalItems > currentItems) && !bottomReached){
      fetchData()
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [requestedPage])

  return (
    <>
      <NavBar />
      <HeroSection />
      {genres && (
        <div className="container">
          {Object.values(genres).map((genre) => (
            <Section key={genre.value} genre={genre.value} />
          ))}
        </div>
      )}
      <div
        className="page-end"
        onMouseEnter={() => {
          setRequestedPage( np => np + 1 )
        }}
      />
    </>
  )
}

export default App
