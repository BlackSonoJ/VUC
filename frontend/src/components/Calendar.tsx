import { FC, useEffect, useState } from 'react';
import { Container } from '../styledComponents/Container';
import { Paragraph } from '../styledComponents/Paragraph';
import { Button } from '../styledComponents/Button';
import axios from 'axios';

const getCurrentMonthAndYear = (month: number, year: number) => {
  const now = new Date(year, month);
  const options: Intl.DateTimeFormatOptions = {
    year: 'numeric',
    month: 'long',
  };
  return now.toLocaleDateString('ru-RU', options);
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

type Events = {
  id: number;
  user: number;
  name: string;
  description: string;
  published: Date;
};

export const Calendar: FC = () => {
  const [currentMonth, setCurrentMonth] = useState(new Date().getMonth());
  const [currentYear, setCurrentYear] = useState(new Date().getFullYear());
  const [events, setEvents] = useState<Events[]>([]);

  const currentMonthAndYear = getCurrentMonthAndYear(currentMonth, currentYear);
  const currentMonthAndYearUpperCase =
    currentMonthAndYear.slice(0, 1).toUpperCase() +
    currentMonthAndYear.slice(1);
  const calendarDays = generateCalendar(currentMonth, currentYear);

  useEffect(() => {
    const handleEvents = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/events');
        console.log(response);
        if (response) {
          setEvents(response.data);
        }
      } catch (err) {
        console.error(err);
      }
    };

    handleEvents();
  }, []);

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

  const isEventDay = (day: number) => {
    return events.some(event => {
      const eventDate = new Date(event.published);
      return (
        eventDate.getDate() === day &&
        eventDate.getMonth() === currentMonth &&
        eventDate.getFullYear() === currentYear
      );
    });
  };

  return (
    <Container
      $width='100%'
      height='fit-content'
    >
      <Container
        $margin='20px 0 20px 0'
        $width='100%'
        display='flex'
        $justify='space-between'
        $align='center'
      >
        <Button
          color='white'
          cursor='pointer'
          onClick={goToPreviousMonth}
        >
          ◀
        </Button>
        <Paragraph
          color='white'
          $fontSize='32px'
        >
          {currentMonthAndYearUpperCase}
        </Paragraph>
        <Button
          color='white'
          cursor='pointer'
          onClick={goToNextMonth}
        >
          ▶
        </Button>
      </Container>

      <Container
        display='grid'
        $gridTemplateColumns='repeat(7, 1fr)'
        $gridTemplateRows='50px repeat(6, 200px)'
        $gap='5px'
      >
        {['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'].map((day, index) => (
          <Container
            key={index}
            $fontWeight='bold'
            $textAlign='center'
            $margin='10px 0 10px 0'
          >
            <Paragraph
              color='white'
              $fontSize='17px'
            >
              {day}
            </Paragraph>
          </Container>
        ))}
        {calendarDays.map((day, index) => (
          <Container
            key={index}
            display='flex'
            $align='flex-start'
            $padding='15px'
            $bgColor={day ? (isEventDay(day) ? 'red' : '#f0f0f0') : '#f0f0f078'}
            $border='1px solid #ddd'
            $borderRadius='5px'
          >
            {day ? day : ''}
          </Container>
        ))}
      </Container>
    </Container>
  );
};
