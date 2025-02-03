import { FC } from "react";
import { Paragraph } from "../styledComponents/Paragraph";
import { Flex } from "../styledComponents/Flex";
import { Link } from "react-router-dom";

type MainPageButtonProps = {
  buttonText: string;
};

export const MainPageButton: FC<MainPageButtonProps> = ({ buttonText }) => {
  return (
    <Link
      to="/"
      style={{
        textDecoration: "none",
        color: "black",
        width: "100%",
        height: "100%",
        gridArea: "1 / 2 / 3 / 3",
      }}
    >
      <Flex
        width="100%"
        height="100%"
        $bgColor="#3fd5fe"
        $justify="center"
        $align="center"
        $borderRadius="3px"
      >
        <Paragraph $fontSize="18px">{buttonText}</Paragraph>
      </Flex>
    </Link>
  );
};
