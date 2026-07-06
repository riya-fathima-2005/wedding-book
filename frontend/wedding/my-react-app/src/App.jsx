import "./App.css";

import { Routes, Route, useLocation } from "react-router-dom";

// NAVBAR & FOOTER
import Nav from "./Components/Navbar/Nav";
import Footer from "./Components/Footer/Footer";

// PAGES
import Home from "./Components/Home/Home";
import Wedding from "./Components/Weddingpage/Wedding";
import Aboutpage from "./Components/AboutPage/Aboutpage";
import Gallery from "./Components/Gallery/Gallery";
import Costume from "./Components/Costumes/Costume";
import Faqcontent from "./Components/Faqpage/Faqcontent";
import Hostsec from "./Components/Host/Hostsec";
import Blogpage from "./Components/Blogpage/Blogpage";

import Subblogss from "./Components/Subblogs/Subblogss";
import Christians from "./Components/Celebrations/Celebrations";
import Contacted from "./Components/Contacting/Contacted";
import Howtohost from "./Components/Howhost/Howtohost";
import Hostdetails from "./Components/Howhost/Hostdetails";
import VenueNearby from "./Components/Venue/VenueNearby";
import NotFound from "./Components/NotFound";


// AUTH
import Login from "./Components/Login/Login";
import Sign from "./Components/Sign/Sign";

// VENUE
import Venue from "./Components/Venue/Venue";
import Venuegallary from "./Components/Venue/Venuegallary";

import Morevenueside from "./Components/Morevenue/Morevenueside";

// MORE VENUE
import Morevenue1 from "./Components/Morevenue/Morevenue1";
import Morevenue2 from "./Components/Morevenue/Morevenue2";
import Morevenue3 from "./Components/Morevenue/Morevenue3";
import Morevenue4 from "./Components/Morevenue/Morevenue4";
import Morevenue5 from "./Components/Morevenue/Morevenue5";
import Morevenue6 from "./Components/Morevenue/Morevenue6";
import Payment from "./Components/Payment/Payments";
import Success from "./Components/Payment/Success";
import WeddingDetails from "./Components/Weddingpage/WeddingDetails";

// RESERVE
import Reserve from "./Components/Morevenue/Reserve";
import MyBookings from "./Components/Morevenue/MyBookings";

// PROTECTED ROUTE
import ProtectedRoute from "./Components/ProtectedRoute";
import Smallprofile from "./Components/Navbar/Smallprofile";

function App() {
  const location = useLocation();

  const validRoutes = [
    "/",
    "/wedding",
    "/faqqq",
    "/about",
    "/gallery",
    "/venue",
    "/host",
    "/blog",
    "/blogs",
    "/christ",
    "/contact",
    "/hostdetails",
    "/howhost",
    "/payment",
    "/payment-success",
    "/wedding-details",
    "/login",
    "/sign",
    "/my-bookings",
    "/reserve",
    "/venuegallary",
    "/Smallprofile",
  ];

const isAdminRoute =
  location.pathname.startsWith("/admin") ||
  location.pathname.startsWith("/django-admin") ||
  location.pathname.startsWith("/api");

const isNotFound =
  !isAdminRoute &&
  !validRoutes.includes(location.pathname) &&
  !location.pathname.startsWith("/morevenue/") &&
  !location.pathname.startsWith("/blogs/") &&
  !location.pathname.startsWith("/wedding-details/");

  const hideLayout =
    location.pathname === "/login" ||
    location.pathname === "/sign" ||
    isNotFound;

  return (
    <>
      {/* NAVBAR */}
      {!hideLayout && <Nav />}

      <Routes>
        <Route path="/" element={<Home />} />


        <Route path="/wedding" element={<Wedding />} />
        <Route path="/faqqq" element={<Faqcontent />} />
        <Route path="/about" element={<Aboutpage />} />
        <Route path="/gallery" element={<Gallery />} />
        <Route path="/venue" element={<VenueNearby />} />
        <Route path="/host" element={<Hostsec />} />
        {/* <Route path="/blog" element={<Blogpage />} /> */}
      <Route path="/blog" element={<Blogpage />} />
<Route path="/blogs/:slug" element={<Subblogss />} />
        <Route path="/christ" element={<Christians />} />
        <Route path="/contact" element={<Contacted />} />
        <Route path="/hostdetails" element={<Hostdetails />} />
        <Route path="/howhost" element={<Howtohost />} />
        <Route path="/payment" element={<Payment />} />
        <Route path="/payment-success" element={<Success />} />
        <Route path="/wedding-details/:id" element={<WeddingDetails />} />
        

        {/* AUTH */}
        <Route path="/login" element={<Login />} />
        <Route path="/sign" element={<Sign />} />

        {/* MORE VENUE */}
        <Route path="/morevenue/:id" element={<Morevenueside />} />

        {/* MY BOOKINGS */}
        <Route path="/my-bookings" element={<MyBookings />} />

        {/* RESERVE */}
        <Route
          path="/reserve"
          element={
            <ProtectedRoute>
              <Reserve />
            </ProtectedRoute>
          }

          
        />

        {/* VENUE GALLERY */}
        <Route path="/venuegallary" element={<Venuegallary />} />
        <Route path="/Smallprofile" element={<Smallprofile />} />

        {/* 404 PAGE - ALWAYS LAST */}
        <Route path="*" element={<NotFound />} />
      </Routes>

      {/* FOOTER */}
      {!hideLayout && <Footer />}
    </>
  );
}

export default App;