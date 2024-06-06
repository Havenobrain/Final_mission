import React, { useMemo } from 'react';
import { useTable } from 'react-table';

const ComplaintTable = ({ data }) => {
  console.log('Complaint data in ComplaintTable:', data); 

  const columns = useMemo(
    () => [
      { Header: 'Зав. № машины', accessor: 'machine.serial_number' },
      { Header: 'Дата отказа', accessor: 'complaint_date' },
      { Header: 'Наработка, м/час', accessor: 'operating_hours' },
      { Header: 'Узел отказа', accessor: 'failure_node.name' },
      { Header: 'Описание отказа', accessor: 'failure_description' },
      { Header: 'Способ восстановления', accessor: 'recovery_method.name' },
      { Header: 'Используемые запасные части', accessor: 'parts_used' },
      { Header: 'Дата восстановления', accessor: 'recovery_date' },
      { Header: 'Время простоя техники', accessor: 'downtime' },
      { Header: 'Сервисная компания', accessor: 'service_company.username' },
    ],
    []
  );

  const tableInstance = useTable({ columns, data });

  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    rows,
    prepareRow,
  } = tableInstance;

  return (
    <table {...getTableProps()} style={{ width: '100%', borderCollapse: 'collapse' }}>
      <thead>
        {headerGroups.map(headerGroup => (
          <tr {...headerGroup.getHeaderGroupProps()} key={headerGroup.id}>
            {headerGroup.headers.map(column => (
              <th {...column.getHeaderProps()} key={column.id} style={{ border: '1px solid black', padding: '5px' }}>
                {column.render('Header')}
              </th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody {...getTableBodyProps()}>
        {rows.map(row => {
          prepareRow(row);
          return (
            <tr {...row.getRowProps()} key={row.id}>
              {row.cells.map(cell => (
                <td {...cell.getCellProps()} key={cell.column.id} style={{ border: '1px solid black', padding: '5px' }}>
                  {cell.render('Cell')}
                </td>
              ))}
            </tr>
          );
        })}
      </tbody>
    </table>
  );
};

export default ComplaintTable;

