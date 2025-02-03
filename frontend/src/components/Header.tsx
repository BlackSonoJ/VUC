import { FC } from "react";
import HeaderComponent from "../styledComponents/Header";
import { Clock } from "./Clock";
import { DateBlock } from "./Date";
import { VUCBFU } from "./VUCBFU";
import Grid from "../styledComponents/Grid";
import { MenuButton } from "./MenuButton";

export const Header: FC = () => {
  return (
    <HeaderComponent $width="100%" $height="150px" $border="1px solid black">
      <Grid>
        <DateBlock />
        <Clock />
        <VUCBFU />
        <MenuButton
          text="Видеоматериалы"
          gridArea="1 / 5 / 2 / 6"
          margin="0 5px 5px 0"
        />
        <MenuButton
          text="Фотоматериалы"
          gridArea=" 1 / 6 / 2 / 7"
          margin="0 0 5px 0"
        />
        <MenuButton text="Календарь событий" gridArea="2 / 5 / 3 / 6" />
        <MenuButton text="Информация" gridArea="2 / 6 / 3 / 7" />
      </Grid>
    </HeaderComponent>
  );
};
