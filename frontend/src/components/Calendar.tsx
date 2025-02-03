import { FC, useState } from "react";
import { Container } from "../styledComponents/Container";
import { Paragraph } from "../styledComponents/Paragraph";
import { Button } from "../styledComponents/Button";

const getCurrentMonthAndYear = (month: number, year: number) => {
  const now = new Date(year, month);
  const options: Intl.DateTimeFormatOptions = {
    year: "numeric",
    month: "long",
  };
  return now.toLocaleDateString("ru-RU", options);
};

const generateCalendar = (month: number, year: number) => {
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  const firstDayOfMonth = new Date(year, month, 1).getDay();
  const startDay = firstDayOfMonth === 0 ? 6 : firstDayOfMonth - 1;

  const daysArray = [];

  for (let i = 0; i < startDay; i++) {
    daysArray.push(null);
  }

  for (let day = 1; day <= daysInMonth; day++) {
    daysArray.push(day);
  }

  const totalCells = daysArray.length;
  const remainingCells = (7 - (totalCells % 7)) % 7;
  for (let i = 0; i < remainingCells; i++) {
    daysArray.push(null);
  }

  return daysArray;
};

export const Calendar: FC = () => {
  const [currentMonth, setCurrentMonth] = useState(new Date().getMonth());
  const [currentYear, setCurrentYear] = useState(new Date().getFullYear());

  const currentMonthAndYear = getCurrentMonthAndYear(currentMonth, currentYear);
  const calendarDays = generateCalendar(currentMonth, currentYear);

  const goToPreviousMonth = () => {
    if (currentMonth === 0) {
      setCurrentMonth(11);
      setCurrentYear(currentYear - 1);
    } else {
      setCurrentMonth(currentMonth - 1);
    }
  };

  const goToNextMonth = () => {
    if (currentMonth === 11) {
      setCurrentMonth(0);
      setCurrentYear(currentYear + 1);
    } else {
      setCurrentMonth(currentMonth + 1);
    }
  };

  return (
    <Container $width="100%" height="fit-content">
      <Container
        $margin="20px 0 20px 0"
        $width="100%"
        display="flex"
        $justify="space-between"
        $align="center"
      >
        <Button color="white" cursor="pointer" onClick={goToPreviousMonth}>
          ◀
        </Button>
        <Paragraph color="white" $fontSize="32px">
          {currentMonthAndYear}
        </Paragraph>
        <Button color="white" cursor="pointer" onClick={goToNextMonth}>
          ▶
        </Button>
      </Container>

      <Container
        display="grid"
        $gridTemplateColumns="repeat(7, 1fr)"
        $gridTemplateRows="50px repeat(6, 150px)"
        $gap="5px"
      >
        {["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"].map((day, index) => (
          <Container
            key={index}
            $fontWeight="bold"
            $textAlign="center"
            $margin="10px 0 10px 0"
          >
            <Paragraph color="white" $fontSize="17px">
              {day}
            </Paragraph>
          </Container>
        ))}
        {calendarDays.map((day, index) => (
          <Container
            key={index}
            display="flex"
            $align="flex-start"
            $padding="15px"
            $bgColor={day ? "#f0f0f0" : "#f0f0f078"}
            $border="1px solid #ddd"
            $borderRadius="5px"
          >
            {day ? day : ""}
          </Container>
        ))}
      </Container>
    </Container>
  );
};
