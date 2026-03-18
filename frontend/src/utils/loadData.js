export const loadCustomerData = (setData) => {
  fetch("/customer_segments.csv")
    .then(res => res.text())
    .then(text => {
      const lines = text.split("\n");
      const headers = lines[0].split(",");

      const result = lines.slice(1).map(line => {
        const values = line.split(",");
        let obj = {};
        headers.forEach((h, i) => {
          obj[h.trim()] = values[i];
        });
        return obj;
      });

      setData(result);
    });
};