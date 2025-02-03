import { FC } from "react";
import { Paragraph } from "../styledComponents/Paragraph";
import { Flex } from "../styledComponents/Flex";

export const DateBlock: FC = () => {
  const today = new Date();

  return (
    <Flex
      width="250px"
      $gridArea="1 / 1 / 2 / 3"
      $justify="center"
      $align="center"
      $margin="0 5px 0 5px"
    >
      <Paragraph $fontSize="3rem">{today.toLocaleDateString()}</Paragraph>
    </Flex>
  );
};
