import {
    Stack,
    Flex,
    Box,
    Heading,
    Tabs,
    TabList,
    TabPanels,
    Tab,
    TabPanel
} from "@chakra-ui/react"
import Kpi from "../component/Kpi";
import Pie from "../component/PoolDistribution";
import Chart from "../component/Chart";
import Trader from "../component/Trader";
import Search from "../component/Search";


const Swap = () => {
    return (
        <Flex align="center" justifyContent="center" flexDir="column">
            <Search />
            <Stack m={10} mt={5} direction={["column", "row"]} spacing="24px">
                <Kpi title="The Largest Swap" />
                <Kpi title="Total Trade Volume" />
                <Kpi title="Total Unique User"/>
                <Kpi title="Total Swap" />
            </Stack>
            <Stack m={10} mt={5} direction={["column", "row"]} spacing="24px">
                <Box w={400} h={400} boxShadow="lg" rounded="md" bg="white" border="1px" borderColor="gray.200" align="center">
                    <center>
                    <Heading as="h4" size="md" m={0} mt={5}>
                        Pool Distribution By Trade Volume
                    </Heading>
                    </center>
                    <Pie />
                </Box>
                <Box w={1000} h={400} flex="1" bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" align="center">
                    <center>
                    <Heading as="h4" size="md" m={0} mb={5} mt={5}>
                        Total Swap
                    </Heading>
                    </center>
                    <Tabs variant="solid-rounded" colorScheme="teal" m={2}>
                    <TabList  m={4}>
                        <Tab>By Date</Tab>
                        <Tab>By Month</Tab>
                        <Tab>Average By Date</Tab>
                        <Tab>Average By Month</Tab>
                    </TabList>
                    <TabPanels>
                        <TabPanel>
                        <Chart />
                        </TabPanel>
                        <TabPanel>
                        <Chart />
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
                                <Tab>Average By Date</Tab>
                                <Tab>Average By Month</Tab>
                            </TabList>
                            <TabPanels>
                                <TabPanel>
                                <Chart />
                                </TabPanel>
                                <TabPanel>
                                <Chart />
                                </TabPanel>
                            </TabPanels>
                        </Tabs>
                    </Box>
                    <Box w={1000} h={400} mb={10} flex="1" bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" align="center">
                        <center>
                            <Heading as="h4" size="md" m={0} mb={5} mt={5}>
                                Total Gas Spent
                            </Heading>
                        </center>
                        <Tabs variant="solid-rounded" colorScheme="teal" m={2}>
                            <TabList  m={4}>
                                <Tab>By Date</Tab>
                                <Tab>By Month</Tab>
                                <Tab>Average By Date</Tab>
                                <Tab>Average By Month</Tab>
                            </TabList>
                            <TabPanels>
                                <TabPanel>
                                <Chart />
                                </TabPanel>
                                <TabPanel>
                                <Chart />
                                </TabPanel>
                            </TabPanels>
                        </Tabs>
                    </Box>
                </Flex>
                <Box w={400} h={800} boxShadow="lg" rounded="md" bg="white" border="1px" borderColor="gray.200" align="center" overflow="auto">
                    <center>
                    <Heading as="h4" size="md" m={0} mt={5}>
                        Top 10 Trader By Volume
                    </Heading>
                    </center>
                    <Flex flexDir="column" align="center" m={10}>
                        <Trader />
                        <Trader />
                        <Trader />
                        <Trader />
                        <Trader />
                        <Trader />
                        <Trader />
                        <Trader />
                        <Trader />
                    </Flex>
                    
                    
                </Box>
            </Stack>
            
        </Flex>
        
    )
}

export default Swap;