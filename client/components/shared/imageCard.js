import image from "next/image";
import Container from "./container";

export default function ImageCard({ imageURL }) {
  return (
    <Container>
      <div className="w-full max-w-4xl mx-auto mb-20 overflow-hidden rounded-2xl">
        <img
          src={imageURL}
          alt="Image"
          className="w-full h-full object-cover"
        />
      </div>
    </Container>
  );
}
