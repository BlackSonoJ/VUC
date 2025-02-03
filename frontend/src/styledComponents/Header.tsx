import { FC } from "react";
import styled from "styled-components";

interface HeaderProps {
  $width: string;
  $height: string;
  $border: string;
  $size: string;
  $weight: string;
  $color: string;
  $align: string;
  $margin: string;
  children: React.ReactNode;
}

const StyledHeader = styled.header<Partial<HeaderProps>>`
  width: ${(props) => props.$width};
  height: ${(props) => props.$height};
  border: ${(props) => props.$border};
  font-size: ${(props) => props.$size};
  font-weight: ${(props) => props.$weight};
  color: ${(props) => props.$color};
  text-align: ${(props) => props.$align};
  margin: ${(props) => props.$margin};
`;
const HeaderComponent: FC<Partial<HeaderProps>> = (props) => {
  return <StyledHeader {...props}>{props.children}</StyledHeader>;
};

export default HeaderComponent;
