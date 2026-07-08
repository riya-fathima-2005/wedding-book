import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

function GoogleSuccess() {
  const navigate = useNavigate();

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);

    const access = params.get("access");
    const refresh = params.get("refresh");

    if (access) {
      localStorage.setItem("token", access);
      localStorage.setItem("refresh", refresh);

      navigate("/");
      window.location.reload();
    }
  }, [navigate]);

  return <p>Logging you in...</p>;
}

export default GoogleSuccess;