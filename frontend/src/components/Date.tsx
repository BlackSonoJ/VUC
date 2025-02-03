import { FC } from "react";
import { Paragraph } from "../styledComponents/Paragraph";
import { Flex } from "../styledComponents/Flex";

export const DateBlock: FC = () => {
  const today = new Date();

  return (
    <Flex
      width="100%"
      $gridArea="1 / 1 / 2 / 2"
      $justify="center"
      $align="center"
      $bgColor="#0c0c23"
    >
      <Paragraph $fontSize="3rem">{today.toLocaleDateString()}</Paragraph>
    </Flex>
  );
};
