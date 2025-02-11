export const getCurrentMonthAndYear = (month: number, year: number) => {
  const now = new Date(year, month);
  return now.toLocaleDateString('ru-RU', { year: 'numeric', month: 'long' });
};

export const generateCalendar = (month: number, year: number) => {
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  const firstDayOfMonth = new Date(year, month, 1).getDay();
  const startDay = firstDayOfMonth === 0 ? 6 : firstDayOfMonth - 1;
  const daysArray = new Array(startDay).fill(null);
  for (let day = 1; day <= daysInMonth; day++) {
    daysArray.push(day);
  }
  while (daysArray.length % 7 !== 0) {
    daysArray.push(null);
  }
  return daysArray;
};
