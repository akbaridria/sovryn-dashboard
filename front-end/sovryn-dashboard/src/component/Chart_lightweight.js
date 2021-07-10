import React, { useEffect } from 'react';
import { createChart } from 'lightweight-charts';

function ChartLight({data}) {
  const ref = React.useRef();

  useEffect(() => {
    const chart = createChart(ref.current, { width: 900, height: 230, 
    rightPriceScale: {
        scaleMargins: {
            top: 0.3,
            bottom: 0.25,
        },
    },
    timeScale: {
        visible: true,
    },
    crosshair: {
        vertLine: {
            width: 5,
            color: 'rgba(224, 227, 235, 0.1)',
            style: 0,
        },
        horzLine: {
            visible: false,
            labelVisible: true,
        },
    },
    localization: {
        priceFormatter: price => {
        const nf = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' })
         return   nf.format(price)
        },


    },    
    grid: {
        vertLines: {
            color: 'rgba(42, 46, 57, 0)',
        },
        horzLines: {
            color: 'rgba(42, 46, 57, 0)',
        },
    },
    });
    const lineSeries = chart.addLineSeries({
        color: 'rgba(0, 128, 128, 1)',
        lineWidth: 2,
    });
    lineSeries.setData(data);
    return () => {
        chart.remove()
      } 
  });

  return (
    <>
      <div ref={ref} />
    </>
  );
}

export default ChartLight;