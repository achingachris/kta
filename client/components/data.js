import {
  EmojiHappyIcon,
  ChartSquareBarIcon,
  CursorClickIcon,
  DeviceMobileIcon,
  AdjustmentsIcon,
  SunIcon,
} from "@heroicons/react/outline";

import benefitOneImg from "../public/img/benefit-one.png";
import benefitTwoImg from "../public/img/benefit-two.png";

const benefitOne = {
  title: "Expand Your Network",
  desc: "Leverage the event to connect with tech leaders, entrepreneurs, and innovators.",
  image: benefitOneImg,
  bullets: [
    {
      title: "Connect with Industry Leaders",
      desc: "Meet and network with top figures in the tech sector.",
      icon: <EmojiHappyIcon />,
    },
    {
      title: "Discover Emerging Trends",
      desc: "Gain insights into the latest tech advancements.",
      icon: <ChartSquareBarIcon />,
    },
    {
      title: "Showcase Your Innovations",
      desc: "Opportunity to present your tech solutions.",
      icon: <CursorClickIcon />,
    },
  ],
};

const benefitTwo = {
  title: "Enhance Your Skills and Knowledge",
  desc: "Use the event to gain valuable industry insights and develop new skills.",
  image: benefitTwoImg,
  bullets: [
    {
      title: "Interactive Workshops",
      desc: "Participate in hands-on sessions for practical learning.",
      icon: <DeviceMobileIcon />,
    },
    {
      title: "Inspirational Talks",
      desc: "Hear from visionary leaders and tech pioneers.",
      icon: <AdjustmentsIcon />,
    },
    {
      title: "Networking Opportunities",
      desc: "Build valuable connections for future collaborations.",
      icon: <SunIcon />,
    },
  ],
};


export { benefitOne, benefitTwo };
