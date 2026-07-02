import React, { useEffect, useState } from "react";
import wed7 from "../../assets/Images/banimgjpj.jpeg";
import { Link, useParams } from "react-router-dom";
import "../../assets/Style/Subblog.css";

const Subblogss = () => {

  const { slug } = useParams();

  const [blog, setBlog] = useState(null);

  const API_URL = "https://wedding-book.onrender.com";
  // local testing:
  // const API_URL = "http://127.0.0.1:8000";

  useEffect(() => {

    fetch(`${API_URL}/api/blogs/${slug}/`)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        setBlog(data);
      })
      .catch((error) => {
        console.log(error);
      });

  }, [slug]);

  // Loading state
  if (!blog) {
    return <h2 style={{ textAlign: "center" }}>Loading...</h2>;
  }

  return (
    <>
      {/* Banner */}

      <div className="container py-5">

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

      </div>


      {/* BLOG CONTENT */}

      <section className="luxury-blog-detail">

        {/* Intro */}

        <div className="article-intro">

          {/* Dynamic Category */}

          <p className="article-category">

            {blog.category}

          </p>


          {/* Dynamic Title */}

          <h2 className="article-main-title">

            {blog.title}

          </h2>

          <div className="article-line"></div>


          {/* Blog Image */}

          <div className="single-blog-image">

            <img
              src={blog.image}
              alt={blog.title}
              style={{
                width: "100%",
                marginBottom: "30px",
                borderRadius: "10px"
              }}
            />

          </div>


          {/* Dynamic Full Content from CKEditor */}

          <div
            className="article-text"

            dangerouslySetInnerHTML={{
              __html: blog.content
            }}
          ></div>

        </div>


        {/* Back Button */}

        <div className="back-btn-wrapper">

          <Link
            to="/blog"
            className="luxury-back-btn"
          >

            Back to Posts

          </Link>

        </div>

      </section>
    </>
  );
};

export default Subblogss;