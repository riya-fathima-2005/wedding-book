import React from "react";
import axios from "axios";
import { useLocation, useNavigate } from "react-router-dom";
import "../../assets/Style/WeddingDetails.css";

const WeddingDetails = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const wedding = location.state;
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
                JSON.parse(localStorage.getItem("user"))?.username ||
                "Guest",

              venue_name: `${wedding.firstname} & ${wedding.partner_firstname}`,

              amount: 999,

              razorpay_order_id: order.id,

              razorpay_payment_id:
                response.razorpay_payment_id,
            }
          );

          alert("🎉 Payment Successful!");

        } catch (error) {
          console.log(error);

          alert("Payment saved failed");
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

        {/* Left Side Image */}
        <div>
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
        </div>

        {/* Right Side */}
        <div className="wedding-body">

          <h2 className="wedding-title1">
            {wedding.firstname} & {wedding.partner_firstname}
          </h2>

          {/* Free Details */}
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

          <div className="description-box">
            <h4>Wedding Story</h4>
            <p>{wedding.description || "No Description Added"}</p>
          </div>

          {/* Premium Card */}
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
 <span style={{ marginLeft: "40px" }}>
   <button
  className="btn btn-dark unlock-btn"
  onClick={handleUnlockPayment}
>
  🔓 Unlock Now
</button>
 </span>


</div>

<div className="premium-note">
  One-time payment. Once purchased, you can access these details anytime.
</div>

          </div>

        </div>
      </div>
    </div>
  );
};


export default WeddingDetails;