import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "../../assets/Style/Login.css";
import logo from "../../assets/Images/logo.png";

const Login = () => {

  const navigate = useNavigate();

  // STATES
  const [username, setUsername] = useState("");

  const [password, setPassword] = useState("");

  const [errorMessage, setErrorMessage] = useState("");

  const [isSuccess, setIsSuccess] = useState(false);

  // HANDLE LOGIN
 const handleSubmit = async (e) => {
  e.preventDefault();

  setErrorMessage("");

  try {
const response = await fetch(
  "https://wedding-book.onrender.com/api/token/",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username,
          password,
        }),
      }
    );

    const text = await response.text();

    const data = text ? JSON.parse(text) : {};

    if (!response.ok) {
      throw new Error(
        data.detail || "Login failed"
      );
    }

    localStorage.setItem(
      "token",
      data.access
    );

    localStorage.setItem(
      "refresh",
      data.refresh
    );

    localStorage.setItem(
      "user",
      JSON.stringify({
        username: username,
      })
    );

    setIsSuccess(true);

    setTimeout(() => {
      navigate("/");
      window.location.reload();
    }, 1000);

  } catch (error) {
    console.error(error);
    setErrorMessage(error.message);
  }
};

  // SUCCESS SCREEN
  if (isSuccess) {

    return (

      <div className="login-success">

        <h2>

          Login Successful

        </h2>

        <p>

          Redirecting...

        </p>

      </div>
    );
  }

  return (

    <div className="login-container">
<form
  className="login-form"
  onSubmit={handleSubmit}
>

  <div className="login-logo">

    <img
      src={logo}
      alt="Logo"
    />

  </div>

  <h2>

    Log In

  </h2>
        {/* ERROR MESSAGE */}
        {errorMessage && (

          <p className="error-message">

            {errorMessage}

          </p>

        )}

        {/* USERNAME */}
        <div className="input-group">

          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) =>
              setUsername(
                e.target.value
              )
            }
            required
          />

        </div>

        {/* PASSWORD */}
        <div className="input-group">

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) =>
              setPassword(
                e.target.value
              )
            }
            required
          />

        </div>

        {/* BUTTON */}
        <button type="submit">

          Login

        </button>

        {/* SIGNUP LINK */}
        <div className="signup-text">

          Don’t have an account? 

          <Link to="/sign">

             <span> Sign Up</span>

          </Link>

        </div>

      </form>

    </div>
  );
};

export default Login;