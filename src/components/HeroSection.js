import { useState, useEffect } from "react"

const HeroSection = () => {
  const [movie, setMovie] = useState(null)
  const pageState = null

  const fetchData = async () => {
    const response = await fetch("/.netlify/functions/getMovies", {
      method: "POST",
      body: JSON.stringify({ genre: "Sci-Fi", pageState: pageState }),
    })
    const responseBody = await response.json()
    const movies = responseBody.data.movies_by_genre.values
    setMovie(movies[Math.floor(Math.random() * movies.length)])
  }

  useEffect(() => {
    fetchData()
  }, [])

  return (
    <>
      {movie && (
        <div className="hero">
          <video className="hero-video" muted controls autoPlay={true} loop>
            <source src={movie.thumbnail} type="video/mp4" />
          </video>

          <div className="info-section">
            <h3 className="hero-blurb">{movie.synopsis}</h3>
            <div className="button-section">
              <div className="button play">
                <span>
                  <i className="fas fa-play"></i>
                </span>
                Play
              </div>
              <div className="button more">
                <span>
                  <i className="fas fa-info-circle"></i>
                </span>
                More info
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  )
}

export default HeroSection
