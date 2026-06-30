import { Link } from "react-router-dom";
import "../../src/assets/Style/NotFound.css";

function NotFound() {
  return (
    <div className="pw404-wrapper">
      <div className="pw404-card">
        <h1 className="pw404-code">404</h1>

        <h2 className="pw404-title">
          Page Not Found
        </h2>

        <p className="pw404-text">
          Looks like this page has vanished from our wedding gallery.
        </p>

        <Link to="/" className="pw404-link">
          <button className="pw404-btn">
            Back To Home
          </button>
        </Link>
      </div>
    </div>
  );
}

export default NotFound;