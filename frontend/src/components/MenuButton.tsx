import { FC } from "react";
import { Flex } from "../styledComponents/Flex";
import { Paragraph } from "../styledComponents/Paragraph";

type MenuButtonProps = {
  text: string;
  gridArea: string;
  margin?: string;
};

export const MenuButton: FC<MenuButtonProps> = ({ text, gridArea, margin }) => {
  return (
    <Flex
      width="150px"
      $justify="center"
      $align="center"
      $bgColor="#2b41fe"
      $gridArea={gridArea}
      $margin={margin}
      $borderRadius="3px"
      cursor="pointer"
    >
      <Paragraph $fontSize="14px">{text}</Paragraph>
    </Flex>
  );
};
