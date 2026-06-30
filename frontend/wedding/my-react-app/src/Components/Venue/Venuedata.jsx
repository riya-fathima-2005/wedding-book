import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../../assets/Style/Venuedata.css";
import wed7 from "../../assets/Images/ban4.png";

function Venuedata({ showBanner = true }) {
  const navigate = useNavigate();
  const API_URL = "https://wedding-book.onrender.com";

  const [venues, setVenues] = useState([]);
  const [loading, setLoading] = useState(true);

  // FETCH VENUES (PUBLIC)
  useEffect(() => {
    const fetchVenues = async () => {
      try {
        const response = await fetch(
          `${API_URL}/api/venues/`
        );

       const data = await response.json();


setVenues(Array.isArray(data) ? data : []);
      } catch (error) {
        console.error(
          "Venue Fetch Error:",
          error
        );
      } finally {
        setLoading(false);
      }
    };

    fetchVenues();
  }, []);

const handleViewVenue = (id) => {
  navigate(`/morevenue/${id}`);
};
  return (
    <section className="venues-section">
      {showBanner && (
        <div className="imagesec">
          <img
            src={wed7}
            alt="Venue Banner"
            className="decore-img"
          />
          <h2 className="overlay-text">
            Venue
          </h2>
        </div>
      )}

      <div className="container">
        <h2 className="venue-main-title">
          Find Your Wedding Venue
        </h2>

        <p className="venue-description">
          Discover beautiful wedding venues
          tailored to your style and
          celebration.
        </p>

        {loading ? (
          <p className="loading-text">
            Loading venues...
          </p>
        ) : venues.length === 0 ? (
          <p className="loading-text">
            No venues found.
          </p>
        ) : (
          <div className="venue-grid">
            {venues.map((venue) => (
              <div
                className="venue-card"
                key={venue.id}
              >
                <div className="venue-image-wrapper">
                  <img
                    src={
                      venue.image
                        ? venue.image.startsWith(
                            "http"
                          )
                          ? venue.image
                          : `${API_URL}${venue.image}`
                        : wed7
                    }
                    alt={venue.name}
                    className="venue-image"
                  />
                </div>

                <div className="venue-content">
                  <h4 className="venue-title">
                    {venue.name}
                  </h4>

                  <p className="venue-location">
                    📍 {venue.location}
                  </p>

                  <div className="couple-name">
                    💍 {venue.bride_name} &{" "}
                    {venue.groom_name}
                  </div>

                  <div className="venue-price">
                    ₹ {venue.price}
                  </div>

                  <div
                    className={
                      venue.status ===
                      "Available"
                        ? "status available"
                        : "status booked"
                    }
                  >
                    {venue.status}
                  </div>

                  <button
                    className="view-btn btn-outline-dark"
                    onClick={() =>
                      handleViewVenue(venue.id)
                    }
                  >
                    View Venue
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </section>
  );
}

export default Venuedata;