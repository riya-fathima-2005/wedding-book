import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

function GoogleSuccess() {
  const navigate = useNavigate();

  useEffect(() => {
    const params = new URLSearchParams(
      window.location.search
    );

    const access = params.get("access");
    const refresh = params.get("refresh");

    if (access) {
      localStorage.setItem("token", access);
      localStorage.setItem("refresh", refresh);

      axios
        .get(
          "https://wedding-book.onrender.com/api/profile/",
          {
            headers: {
              Authorization: `Bearer ${access}`,
            },
          }
        )
        .then((res) => {
          localStorage.setItem(
            "user",
            JSON.stringify(res.data)
          );

          navigate("/");
          window.location.reload();
        })
        .catch(() => {
          navigate("/");
        });
    } else {
      navigate("/login");
    }
  }, [navigate]);

  return <h2>Logging in...</h2>;
}

export default GoogleSuccess;