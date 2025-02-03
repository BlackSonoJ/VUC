import { FC } from "react";
import styled from "styled-components";

interface ImgProps {
  width: string;
  height: string;
  $cover: string;
  $margin: string;
  src: string;
  loading: "eager" | "lazy";

  alt: string;
}

const StyledImg = styled.img<Partial<ImgProps>>`
  width: ${(props) => (props.width ? props.width : "auto")};
  height: ${(props) => (props.height ? props.height : "auto")};
  object-fit: ${(props) => props.$cover || "cover"};
  margin: ${(props) => props.$margin || "0"};
  alt: ${(props) => props.alt || ""};
`;

export const Image: FC<Partial<ImgProps>> = (props) => {
  return <StyledImg {...props} />;
};
