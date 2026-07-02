import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import wed7 from "../../assets/Images/banimgjpj.jpeg";
import "../../assets/Style/Blog.css";

const Blog = () => {

  const [blogs, setBlogs] = useState([]);

  // Backend API URL
  const API_URL = "https://wedding-book.onrender.com";
  // For local testing:
  // const API_URL = "http://127.0.0.1:8000";


  useEffect(() => {

  console.log("useEffect running");

  fetch(`${API_URL}/api/blogs/`)
    .then((res) => {
      console.log("Response:", res);
      return res.json();
    })
    .then((data) => {
      console.log("DATA:", data);
      setBlogs(data);
    })
    .catch((error) => {
      console.log("ERROR:", error);
    });

}, []);

  return (
    <>
      {/* Banner Section */}
      <div className="banner-wrapper">

        <div className="banner-box">

          <img
            src={wed7}
            alt="decor"
            className="decore-img"
          />

          <div className="banner-overlay"></div>

          <div className="banner-content">

            <h2 className="overlay-text">
              BLOG
            </h2>

          </div>

        </div>

      </div>


      {/* Blog Section */}

      <div className="luxury-blog-section">

        <div className="container">

          <div className="blog-heading-area text-center">

            <p className="blog-subtitle">
              OUR JOURNAL
            </p>

            <h2 className="blog-main-heading">
              Stories & Wedding Traditions
            </h2>

          </div>


          {/* If no blogs */}

          {blogs.length === 0 ? (

            <h3 style={{ textAlign: "center" }}>
              No Blogs Available
            </h3>

          ) : (

            <div className="row gy-5">

              {blogs.map((blog) => (

                <div
                  className="col-lg-6"
                  key={blog.id}
                >

                  <div className="luxury-blog-card">

                    {/* Blog Image */}

                    <div className="blog-image-wrapper">

                      <img
                        src={blog.image}   
                        alt={blog.title}
                      />

                    </div>


                    {/* Blog Content */}

                    <div className="blog-content">

                      <span className="blog-category">

                        {blog.category}

                      </span>

                      <h3>

                        {blog.title}

                      </h3>

                      <div>

                        {blog.short_description}

                      </div>


                      <Link
                        to={`/blogs/${blog.slug}`}
                        className="luxury-btn"
                      >

                        Read Article

                      </Link>

                    </div>

                  </div>

                </div>

              ))}

            </div>

          )}

        </div>

      </div>

    </>
  );
};

export default Blog;