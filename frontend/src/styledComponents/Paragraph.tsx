import React, { FC } from "react";
import styled from "styled-components";

interface PragraphProps {
  color?: string;
  $wrap?: "normal" | "anywhere" | "break-word";
  $maxLines?: number;
  $fontSize?: string;
  $textAlign?: string;
  $margin?: string;
  children: React.ReactNode;
}

const StyledParagraph = styled.p<PragraphProps>`
  color: ${(props) => props.color || "white"};
  font-size: ${(props) => props.$fontSize || "12px"};
  text-align: ${(props) => props.$textAlign || "center"};
  overflow: hidden;
  margin: ${(props) => props.$margin};
`;

export const Paragraph: FC<PragraphProps> = (props) => {
  return <StyledParagraph {...props}>{props.children}</StyledParagraph>;
};
