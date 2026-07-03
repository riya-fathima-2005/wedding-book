import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import wed7 from "../../assets/Images/banimgjpj.jpeg";
import "../../assets/Style/Subblog.css";

const Subblog = () => {

  const { slug } = useParams();

  const [blog, setBlog] = useState(null);

  const API_URL = "https://wedding-book.onrender.com";
  // const API_URL = "http://127.0.0.1:8000";

  useEffect(() => {

    fetch(`${API_URL}/api/blogs/${slug}/`)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setBlog(data);
      })
      .catch((err) => {
        console.log(err);
      });

  }, [slug]);

  if (!blog) {
    return (
      <h2 style={{ textAlign: "center", marginTop: "100px" }}>
        Loading...
      </h2>
    );
  }

  return (
    <div>

      {/* Banner */}

      <div className="banner-wrapper bannerblog">

        <div className="banner-box">

          <img
            src={wed7}
            alt="decor"
            className="decore-img"
          />

          <div className="banner-overlay"></div>

          <div className="banner-content">

            <h2
              style={{
                marginLeft: "-720px",
                fontSize: "35px",
                fontFamily: "Cormorant Garamond, serif",
                color: "white"
              }}
            >
              HOME / BLOG
            </h2>

          </div>

        </div>

      </div>


      {/* Main Content */}

      <div className="container py-5">

        {/* Image + Intro */}

        <div className="row mb-5 align-items-center">

          <div className="col-md-6">

            <img
              src={blog.image}
              alt={blog.title}
              className="img-fluid rounded"
            />

          </div>

          <div className="col-md-6">

            <h2 className="dynamic-blog-title">

              {blog.title}

            </h2>

            <div className="dynamic-blog-description">

              {blog.short_description}

            </div>

          </div>

        </div>


        {/* Full CKEditor Content */}

        <div
          className="dynamic-blog-content"
          dangerouslySetInnerHTML={{
            __html: blog.content
          }}
        ></div>


        {/* Back Button */}

        <div className="text-center py-5">

          <Link
            to="/blog"
            className="luxury-back-btn"
          >
            Back to Posts
          </Link>

        </div>

      </div>

    </div>
  );
};

export default Subblog;