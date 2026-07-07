import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import "../../src/assets/Style/DynamicPage.css";
const DynamicPage = () => {
  const { slug } = useParams();

  const [page, setPage] = useState(null);

  useEffect(() => {
    axios
      axios.get("https://wedding-book.onrender.com/api/pages/")
      .then((response) => {
        setPage(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, [slug]);

  if (!page) {
    return (
      <div style={{ padding: "120px 40px" }}>
        Loading...
      </div>
    );
  }

 return (
  <>
    {/* Banner */}

    <section className="cms-banner">

      <div className="cms-overlay">

        <h1>{page.title}</h1>

      </div>

    </section>

    {/* Content */}

    <section className="cms-content">

      <div className="cms-container">

        <div className="cms-card">

          <h2>{page.title}</h2>

          <div
            className="cms-description"
            dangerouslySetInnerHTML={{
              __html: page.content,
            }}
          />

        </div>

      </div>

    </section>
  </>
);

};

export default DynamicPage;