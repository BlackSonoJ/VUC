import { FC } from "react";
import HeaderComponent from "../styledComponents/Header";
import { Clock } from "./Clock";
import { DateBlock } from "./Date";
import { Flex } from "../styledComponents/Flex";

export const Header: FC = () => {
  return (
    <HeaderComponent $width="100%" $height="200px" $border="1px solid black">
      <Flex height="200px" $direction="column" $justify="space-between">
        <DateBlock />
        <Clock />
      </Flex>
    </HeaderComponent>
  );
};
