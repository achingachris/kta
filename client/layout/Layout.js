import Navbar from "./navbar";
import Footer from "./footer";
import Head from "next/head";
const Layout = ({ children }) => {
  return (
    <>
    <Head>
        <title>Kenya Tech Awards</title>
        <meta
          name="description"
          content="
          Kenya Tech Awards offers a unique forum in which academics, educators, start-ups, entrepreneurs, policymakers and students share their stories with fellow interest groups to quench their
          thirst for Innovative Solutions in the tech sector."
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Navbar />
      {children}
      <Footer />
    </>
  );
};

export default Layout;
