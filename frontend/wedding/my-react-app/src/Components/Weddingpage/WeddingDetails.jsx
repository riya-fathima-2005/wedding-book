import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";
import "../../assets/Style/WeddingDetails.css";

const WeddingDetails = () => {
  const navigate = useNavigate();
  const { id } = useParams();

  const [wedding, setWedding] = useState(null);
  const [unlocked, setUnlocked] = useState(false);

  console.log("Route ID:", id);

  useEffect(() => {
    const fetchWedding = async () => {
      try {
        console.log("Fetching:", `https://wedding-book.onrender.com/api/weddings/${id}/`);

        const response = await axios.get(
          `https://wedding-book.onrender.com/api/weddings/${id}/`
        );

        console.log("Wedding Response:", response.data);

        setWedding(response.data);

      } catch (error) {
        console.log("API Error:", error.response);
      }
    };

    fetchWedding();
  }, [id]);

  useEffect(() => {

    if (!wedding) return;

const checkPayment = async () => {
  try {
    const username = JSON.parse(localStorage.getItem("user"))?.username;

    console.log("Username:", username);
    console.log("Wedding ID:", wedding.id);

    const response = await axios.get(
      `https://wedding-book.onrender.com/has-paid/${wedding.id}/`,
      {
        params: { username },
      }
    );

    console.log("Has Paid Response:", response.data);

    if (response.data.paid) {
      console.log("Unlocking...");
      setUnlocked(true);
    } else {
      console.log("Still locked");
    }

  } catch (error) {
    console.log(error);
  }
};

    checkPayment();

  }, [wedding]);

  const handleUnlockPayment = async () => {
    try {
      const paymentResponse = await axios.post(
        "https://wedding-book.onrender.com/create-payment/",
        {
          amount: 999,
        }
      );

      const order = paymentResponse.data;

     const options = {
  key: "rzp_test_SyG00JPy3MbhJq",
  amount: order.amount,
  currency: order.currency,
  order_id: order.id,

  name: "Wedding Book",
  description: "Unlock Premium Wedding Details",

  handler: async function (response) {
    try {
      await axios.post(
        "https://wedding-book.onrender.com/save-payment/",
        {
          payer_name:
            JSON.parse(localStorage.getItem("user"))?.username || "Guest",

          venue_name: `${wedding.firstname} & ${wedding.partner_firstname}`,

          wedding: wedding.id,

          amount: 999,

          razorpay_order_id: order.id,

          razorpay_payment_id: response.razorpay_payment_id,
        }
      );

      alert("🎉 Payment Successful!");

      setUnlocked(true);

    } catch (error) {
      console.log(error);
      alert("Payment save failed");
    }
  },

  theme: {
    color: "#000000",
  },
};

const razorpay = new window.Razorpay(options);

razorpay.open();

    } catch (error) {
      console.log(error);

      alert("Unable to start payment.");
    }
  };

  if (!wedding) {
    return (
      <div className="container mt-5">
        <h3>No Wedding Details Found</h3>
      </div>
    );
  }




  return (
    <div className="wedding-details-page1">

      <div className="wedding-profile-page">

      {/* Left Side */}

<div className="wedding-left-panel">

  {wedding.profile_image ? (
    <img
      src={wedding.profile_image}
      alt="Wedding"
      className="wedding-image1"
    />
  ) : (
    <img
      src="https://picsum.photos/400/500"
      alt="No Image"
      className="wedding-image1"
    />
  )}

  <div className="couple-card">

    <h3>
      {wedding.firstname} & {wedding.partner_firstname}
    </h3>

    <p>{wedding.wedding_date}</p>

  </div>

</div>

        {/* Right Side */}
        <div className="wedding-body">

         <div className="title-section">

  <p className="title-tag">
    WEDDING EXPERIENCE
  </p>

  <h1 className="wedding-title1">
    {wedding.firstname}
    <span className="ampersand"> & </span>
    {wedding.partner_firstname}
  </h1>

  <div className="title-divider"></div>

</div>
          {/* FREE DETAILS */}

         <div className="detail-grid">

  <div className="detail-box">
    <strong>Wedding Date</strong>
    <p>{wedding.wedding_date || "Not Added"}</p>
  </div>

  <div className="detail-box">
    <strong>Food Type</strong>
    <p>{wedding.food_type || "Not Added"}</p>
  </div>

  <div className="detail-box">
    <strong>Language</strong>
    <p>{wedding.language || "Not Added"}</p>
  </div>

</div>

        <div className="story-card">

  <h3>Wedding Story</h3>

  <p>
    {wedding.description || "No Description Added"}
  </p>

</div>

          {/* PREMIUM SECTION */}

          {!unlocked ? (

            <div className="premium-lock-card">

              <h3>🔒 Premium Wedding Details</h3>

              <p>
                Unlock complete wedding information with a one-time payment.
              </p>

              <ul className="premium-list">
                <li>✔ Wedding Venue</li>
                <li>✔ Contact Number</li>
                <li>✔ Email Address</li>
                <li>✔ Full Address</li>
                <li>✔ Google Map Location</li>
                <li>✔ Download Invitation Card</li>
              </ul>

              <h2 className="premium-price">
                ₹999
              </h2>

              <div className="premium-btn-group">

                <button
                  className="btn btn-dark back-btn"
                  onClick={() => navigate(-1)}
                >
                   Back
                </button>

                <button
                  className="btn btn-dark back-btn" style={{ marginLeft: "25px" }}
                  onClick={handleUnlockPayment}
                >
                  🔓 Unlock Now
                </button>

              </div>

              <div className="premium-note">
                One-time payment. Once purchased you can access these details anytime.
              </div>

            </div>

          ) : (

            <div className="premium-lock-card">

              <h2> Premium Details Unlocked</h2>

              <div className="detail-box">
                <strong>Bride & Groom</strong>
                <p>
                  {wedding.firstname} & {wedding.partner_firstname}
                </p>
              </div>

              <div className="detail-box">
                <strong>Email</strong>
                <p>{wedding.email}</p>
              </div>

              <div className="detail-box">
                <strong>Phone Number</strong>
                <p>{wedding.phone}</p>
              </div>

              <div className="detail-box">
                <strong>Wedding Venue</strong>
                <p>{wedding.custom_venue}</p>
              </div>

              <div className="detail-box">
                <strong>Manager Contact</strong>
                <p>{wedding.manager_phone || "Not Added"}</p>
              </div>

              {wedding.latitude && wedding.longitude && (

                <a
                  href={`https://www.google.com/maps?q=${wedding.latitude},${wedding.longitude}`}
                  target="_blank"
                  rel="noreferrer"
                  className="btn btn-dark mt-3"
                >
                  View Location
                </a>

              )}
{wedding.invitation && (
  <a
    href={wedding.invitation}
    target="_blank"
    rel="noreferrer"
    download
    className="btn btn-dark mt-3"
  >
    Download Invitation
  </a>
)}
            </div>

          )}

        </div>

      </div>

    </div>
  );
};

export default WeddingDetails;