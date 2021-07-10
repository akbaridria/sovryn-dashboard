import {
    Stack,
    Flex,
    Box,
    Heading,
    Tabs,
    TabList,
    TabPanels,
    Tab,
    TabPanel,
    Alert,
    AlertIcon,
    Badge,
    AlertTitle,
    AlertDescription
} from "@chakra-ui/react"
import Kpi from "../component/Kpi";
import Pie from "../component/PoolDistribution";
import Chart from "../component/Chart";
import Trader from "../component/Trader";
import Search from "../component/Search";
import React from "react";
import axios from "axios";
import ChartLight from "../component/Chart_lightweight";

const Swap = () => {
    
    const [largestSwap, setLargestSwap] = React.useState(0)
    const [tradeVolume, setTradeVolume] = React.useState(0)
    const [totalUser, setTotalUser] = React.useState(0)
    const [totalSwap, setTotalSwap] = React.useState(0)
    const [dataPie, setDataPie] = React.useState([])
    const [dataSwapDate, setDataSwapDate] = React.useState([])
    const [dataSwapMonth, setDataSwapMonth] = React.useState([])
    const [dataUserDate, setDataUserDate] = React.useState([])
    const [dataUserMonth, setDataUserMonth] = React.useState([])
    const [dataGasDate, setDataGasDate] = React.useState([])
    const [dataGasMonth, setDataGasMonth] = React.useState([])
    const [topTraders, setTopTraders] = React.useState([])


    React.useEffect(() => {
        get_data_swap();
        
    }, [])

    function processDataPool(raw) {
        let tempPool = []
        raw.data.map((val) => {
                for(var i in val) {
                    tempPool.push({ name : i, value : val[i]})
                }
            })
        return tempPool
    }

    function getLast7Days(raw) {
        let tempData = []
        for(let i = 0; i < raw.data.length;i++) {
            let month = new Date(raw.data[i].date).getMonth()+1
            tempData.push({
                time : new Date(raw.data[i].date).getFullYear() +"-"+month+"-"+new Date(raw.data[i].date).getDate(),
                value : raw.data[i]['SUM(total_value_usd)']
            })
        }
        return tempData
    }

    function changeForRechart(raw) {
        let tempData = []
        for(let i = 0; i < raw.data.length;i++) {
            
            tempData.push({
                date : raw.data[i].month,
                total : raw.data[i].volume
            })
        }
        return tempData
    }

    function changeForRechartUser(raw) {
        let tempData = []
        for(let i = 0; i < raw.data.length;i++) {
            
            tempData.push({
                date : raw.data[i].date,
                total : raw.data[i].unique_swapper
            })
        }
        return tempData
    }

    function changeForRechartUserMonth(raw) {
        let tempData = []
        for(let i = 0; i < raw.data.length;i++) {
            let monthTemp = new Date(raw.data[i].date).getMonth() + 1
            tempData.push({
                date : monthTemp,
                total : raw.data[i].unique_swapper
            })
        }
        return tempData
    }

    function changeForRechartGasDate(raw) {
        let tempData = []
        for(let i = 0; i < raw.data.length;i++) {
            
            tempData.push({
                date : raw.data[i].date,
                total : raw.data[i].volume
            })
        }
        return tempData
    }
    async function get_data_swap(paramFilter='') {
        const url_kpi = axios.get("https://api-sovryn.akbaridria.com/api/get_kpi_swap" + paramFilter)
        const url_distribution = axios.get("https://api-sovryn.akbaridria.com/api/get_swap_distribution" + paramFilter)
        const url_total_swap_date = axios.get("https://api-sovryn.akbaridria.com/api/get_total_swap" + paramFilter)
        const url_total_swap_month = axios.get("https://api-sovryn.akbaridria.com/api/get_swap_month" + paramFilter)
        const url_total_user_date = axios.get("https://api-sovryn.akbaridria.com/api/get_swap_user" + paramFilter)
        const url_total_user_month = axios.get("https://api-sovryn.akbaridria.com/api/get_swap_user_month" + paramFilter)
        const url_total_gas_date = axios.get("https://api-sovryn.akbaridria.com/api/get_spent_gas_date" + paramFilter)
        const url_total_gas_month = axios.get("https://api-sovryn.akbaridria.com/api/get_spent_gas_month" + paramFilter)
        const url_top_trader = axios.get("https://api-sovryn.akbaridria.com/api/top_trader" + paramFilter)
        await axios.all([url_kpi, url_distribution, url_total_swap_date, url_total_swap_month, url_total_user_date, url_total_user_month, url_total_gas_date, url_total_gas_month, url_top_trader])
        .then((...responses) => {
            console.log("oke gan mantap jiwa")
            const data_kpi = responses[0][0]
            const dataPool = responses[0][1]
            const rawDataSwapDate = responses[0][2]
            const rawDataSwapMonth = responses[0][3]
            const rawDataUserDate = responses[0][4]
            const rawDataUserMonth = responses[0][5]
            const rawDataGasDate = responses[0][6]
            const rawDataGasMonth = responses[0][7]
            const topTrader = responses[0][8]
            setTopTraders(topTrader.data)
            setDataGasMonth(changeForRechart(rawDataGasMonth))
            setDataGasDate(changeForRechartGasDate(rawDataGasDate))
            setDataUserMonth(changeForRechartUserMonth(rawDataUserMonth))
            setDataUserDate(changeForRechartUser(rawDataUserDate))
            setDataSwapMonth(changeForRechart(rawDataSwapMonth))
            setDataSwapDate(getLast7Days(rawDataSwapDate))
            setDataPie(processDataPool(dataPool))
            setLargestSwap(data_kpi.data.largest_swap)
            setTradeVolume(data_kpi.data.total_volume)
            setTotalUser(data_kpi.data.total_unique)
            setTotalSwap(data_kpi.data.total_transaction)
        }).catch((error) => {
            console.log(error)
        })
    }

    return (
        <Flex align="center" justifyContent="center" flexDir="column" mt={40}>
            <Search />
            <Alert status="success" width={1380} variant="left-accent">
            <AlertIcon />
            <Box flex="1">
                <AlertTitle>Only Cover</AlertTitle>
                <AlertDescription display="block">
                <Badge variant="solid" mr={2}>RBTC-DOC</Badge><Badge variant="solid" mr={2}>RBTC-BPRO</Badge><Badge variant="solid" mr={2}>RBTC-RUSDT</Badge><Badge variant="solid" mr={2}>RBTC-SOV</Badge>
                </AlertDescription>
            </Box>
                <AlertTitle>Latest Sync Block</AlertTitle>
                <AlertDescription display="block">
                <Badge variant="solid" mr={2}>3141234123</Badge>
                </AlertDescription>   
            </Alert>
            
            <Stack m={10} mt={5} direction={["column", "row"]} spacing="24px">
                <Kpi title="The Largest Swap" total={largestSwap} symbol="$" />
                <Kpi title="Total Trade Volume" total={tradeVolume} symbol="$" />
                <Kpi title="Total Unique User" total={totalUser} symbol="" />
                <Kpi title="Total Swap" total={totalSwap} symbol="" />
            </Stack>
            <Stack m={10} mt={5} direction={["column", "row"]} spacing="24px">
                <Box w={400} h={400} boxShadow="lg" rounded="md" bg="white" border="1px" borderColor="gray.200" align="center">
                    <center>
                    <Heading as="h4" size="md" m={0} mt={5}>
                        Pool Distribution By Trade Volume
                    </Heading>
                    </center>
                    <Pie data={dataPie}/>
                </Box>
                <Box w={1000} h={400} flex="1" bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" align="center">
                    <center>
                    <Heading as="h4" size="md" m={0} mb={5} mt={5}>
                        Total Swap By Volume
                    </Heading>
                    </center>
                    <Tabs variant="solid-rounded" colorScheme="teal" m={2}>
                    <TabList  m={4}>
                        <Tab>By Date</Tab>
                        <Tab>By Month</Tab>
                    </TabList>
                    <TabPanels>
                        <TabPanel>
                        <ChartLight data={dataSwapDate} />
                        </TabPanel>
                        <TabPanel>
                        <Chart data={dataSwapMonth} />
                        </TabPanel>
                    </TabPanels>
                    </Tabs>
                </Box>
            </Stack>
            <Stack m={10} mt={5} direction={["column", "row"]} spacing="24px">
                <Flex flexDir="column">
                    <Box w={1000} h={400} mb={10} flex="1" bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" align="center">
                        <center>
                            <Heading as="h4" size="md" m={0} mb={5} mt={5}>
                                Total Unique User
                            </Heading>
                        </center>
                        <Tabs variant="solid-rounded" colorScheme="teal" m={2}>
                            <TabList  m={4}>
                                <Tab>By Date</Tab>
                                <Tab>By Month</Tab>
                            </TabList>
                            <TabPanels>
                                <TabPanel>
                                <Chart data = {dataUserDate} />
                                </TabPanel>
                                <TabPanel>
                                <Chart data = {dataUserMonth} />
                                </TabPanel>
                            </TabPanels>
                        </Tabs>
                    </Box>
                    <Box w={1000} h={400} mb={10} flex="1" bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" align="center">
                        <center>
                            <Heading as="h4" size="md" m={0} mb={5} mt={5}>
                                Total Gas Spent in USD
                            </Heading>
                        </center>
                        <Tabs variant="solid-rounded" colorScheme="teal" m={2}>
                            <TabList  m={4}>
                                <Tab>By Date</Tab>
                                <Tab>By Month</Tab>
                            </TabList>
                            <TabPanels>
                                <TabPanel>
                                <Chart data={dataGasDate} />
                                </TabPanel>
                                <TabPanel>
                                <Chart data={dataGasMonth} />
                                </TabPanel>
                            </TabPanels>
                        </Tabs>
                    </Box>
                </Flex>
                <Box w={400} h={800} boxShadow="lg" rounded="md" bg="white" border="1px" borderColor="gray.200" align="center" overflow="auto" > 
                    <center>
                    <Heading as="h4" size="md" m={0} mt={5}>
                        Top 10 Trader By Volume
                    </Heading>
                    </center>
                    <Flex flexDir="column" align="center" m={5}>
                        {
                            topTraders.map((val) => {
                                return <Trader data={val} />
                            })
                        }
                        
                    </Flex>
                    
                    
                </Box>
            </Stack>
            
        </Flex>
        
    )
}

export default Swap;