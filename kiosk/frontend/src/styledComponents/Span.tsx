import { FC } from "react";
import styled from "styled-components";

interface SpanProps {
  display?: string;
  width?: string;
  height?: string;
  $size?: string;
  $weight?: string;
  color?: string;
  $decoration?: string;
  $align?: string;
  $marginTop?: string;
  $marginRight?: string;
  $marginBottom?: string;
  children: React.ReactNode;
}

const StyledSpan = styled.span<SpanProps>`
  display: ${(props) => props.display || "inline"};
  font-size: ${(props) => props.$size};
  font-weight: ${(props) => props.$weight};
  color: ${(props) => props.color};
  width: ${(props) => props.width};
  height: ${(props) => props.height};
  text-decoration: ${(props) => props.$decoration || "none"};
  text-align: ${(props) => props.$align};
  margin-top: ${(props) => props.$marginTop || "0"};
  margin-right: ${(props) => props.$marginRight || "0"};
  margin-bottom: ${(props) => props.$marginBottom || "0"};
`;

export const Span: FC<SpanProps> = (props) => {
  return <StyledSpan {...props}>{props.children}</StyledSpan>;
};
