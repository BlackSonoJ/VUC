import { FC } from "react";
import { Link } from "../styledComponents/Link";
import { Paragraph } from "../styledComponents/Paragraph";
import { Flex } from "../styledComponents/Flex";

export const VUCBFU: FC = () => {
  return (
    <Link
      href="https://kantiana.ru/universitys/voennyy-uchebnyy-tsentr/"
      $decoration="none"
      color="black"
      $width="200px"
      $height="100%"
      $gridArea="1 / 3 / 3 / 5"
    >
      <Flex
        width="200px"
        height="100%"
        $bgColor="#3fd5fe"
        $justify="center"
        $align="center"
        $borderRadius="3px"
      >
        <Paragraph $fontSize="18px">Страница ВУЦ БФУ</Paragraph>
      </Flex>
    </Link>
  );
};
