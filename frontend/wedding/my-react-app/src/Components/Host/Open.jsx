import React from "react";
import wed7 from "../../assets/Images/banimgjpj.jpeg";
import "../../assets/Style/Open.css";
import { useNavigate } from "react-router-dom";

const Open = () => {
  const navigate = useNavigate();

  const handleRegister = () => {
    const token = localStorage.getItem("token");

    if (!token) {
      navigate("/login");   // login ഇല്ലെങ്കിൽ login page
    } else {
      navigate("/howhost"); // login ഉണ്ടെങ്കിൽ continue
    }
  };

  return (
    <div className="banner-wrapper">
      <div className="banner-box">
        <img
          src={wed7}
          alt="banner"
          className="decore-img"
        />

        <div className="banner-overlay"></div>

        <div className="content-card">
          <h2
            className="banner-title"
            style={{ fontSize: "35px" }}
          >
            BECOME A HOST
          </h2>

          <p className="banner-text">
            Join hands, share smiles, and welcome the
            world to your special day.
          </p>

          <button
            onClick={handleRegister}
            className="faq-button border-0"
          >
            Register Your Wedding
          </button>
        </div>
      </div>
    </div>
  );
};

export default Open;