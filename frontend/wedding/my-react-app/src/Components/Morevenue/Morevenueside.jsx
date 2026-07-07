import React, {
  useEffect,
  useState
} from "react";
import Swal from "sweetalert2";
import {
  useParams,
  useNavigate
} from "react-router-dom";

import "../../assets/Style/Morevenue1.css";

const Morevenueside = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [venue, setVenue] =
    useState(null);

  const API_URL = "https://wedding-book.onrender.com"

  useEffect(() => {

    const fetchVenue =
      async () => {

        try {

          const response =
  await fetch(
    `${API_URL}/api/venues/`
  );

          const data =
            await response.json();

          const selectedVenue =
            data.find(

              (item) =>
                String(item.id) ===
                String(id)

            );

          setVenue(
            selectedVenue
          );

        } catch (error) {

          console.log(error);

        }

      };

    fetchVenue();

  }, [id]);
const handleReserve = () => {
  navigate("/reserve", {
    state: {
      venueId: venue.id,
      venueName: venue.name,
      venuePrice: venue.price,
    },
  });
};


  if (!venue) {

    return (

      <div className="loading-page">

        <h2>
          Loading Venue...
        </h2>

      </div>

    );

  }

  return (

<div className="split-page">

  <div className="split-card">

    {/* LEFT IMAGE */}

    <div className="split-image-section">

     <img
  src={venue.image}
  alt={venue.name}
  className="split-image"
/>

    </div>

    {/* RIGHT CONTENT */}

    <div className="split-content">

  <h1 className="split-title">
    {venue.name}
  </h1>

  <p className="split-location">
    📍 {venue.location}
  </p>

  <h4 className="split-couple">
    💍 {venue.bride_name} & {venue.groom_name}
  </h4>
     
    <div>
  <h2 className="split-price">
    ₹ {venue.price}
  </h2>

  <div className="split-status">
    {venue.status === "Available" ? (
      <span className="status-green">
        Available
      </span>
    ) : (
      <span className="status-red">
        Booked
      </span>
    )}
    </div>
  </div>

  {/* Accordion Style Description */}

  <details className="about-box" open>
    <summary>
      About Venue
    </summary>

    <p>
      {venue.description}
    </p>

  </details>

  {/* Feature Cards */}

  <div className="feature-grid">

    <div className="feature-card">
      🌸 Premium Decoration
    </div>

    <div className="feature-card">
      ⛵ Exclusive Boat Arrival
    </div>

    <div className="feature-card">
      🍽️ Catering Available
    </div>

    <div className="feature-card">
      💆 Ayurvedic Couple Spa
    </div>

    <div className="feature-card">
      📸 Photo Friendly
    </div>

    <div className="feature-card">
      🍲 Local Cuisine Tasting
    </div>

  </div>

<button
  className="reserve-btn"
  onClick={handleReserve}
>
  Reserve Venue
</button>

</div>

  </div>

</div>
  );

};

export default Morevenueside;