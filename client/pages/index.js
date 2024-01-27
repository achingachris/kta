import Layout from "../layout/Layout";
import Hero from "../components/homePage/hero";
import SectionTitle from "../components/shared/sectionTitle";
import { benefitOne, benefitTwo } from "../data/data";
import ImageCard from "../components/shared/imageCard";
import Benefits from "../components/homePage/benefits";
import Cta from "../components/homePage/cta";
import Faq from "../components/homePage/faq";
import PopupWidget from "../components/homePage/popupWidget";

//import dynamic from "next/dynamic";

// const Video = dynamic(() => import("../components/video"));

// const Benefits = dynamic(() => import("../components/benefits"));
// const Footer = dynamic(() => import("../components/footer"));
// const Testimonials = dynamic(() => import("../components/testimonials"));
// const Cta = dynamic(() => import("../components/cta"));
// const Faq = dynamic(() => import("../components/faq"));

// const PopupWidget = dynamic(() => import("../components/popupWidget"));

export default function Home() {
  return (
    <Layout>
      <Hero />
      <SectionTitle pretitle="KTA Benefits" title=" Why be part of us">
        Attending the Kenya Tech Awards offers networking with industry leaders,
        exposure to innovative tech trends, and opportunities for recognition
        and collaboration in Kenya's vibrant tech sector.
      </SectionTitle>
      <Benefits data={benefitOne} />
      <Benefits imgPos="right" data={benefitTwo} />
      <SectionTitle
        pretitle="Discover the Future"
        title="Experience the Impact of Technology"
      >
        Highlighting the transformative power of tech, this section showcases a
        dynamic video about the Kenya Tech Awards.
      </SectionTitle>
      <ImageCard imageURL="/brand/logo-bg.jpg" />
      <SectionTitle pretitle="FAQ" title="Frequently Asked Questions">
        Answer your customers possible questions here, it will increase the
        conversion rate as well as support or chat requests.
      </SectionTitle>
      <Faq />
      <Cta />
      <PopupWidget />
    </Layout>
  );
}
