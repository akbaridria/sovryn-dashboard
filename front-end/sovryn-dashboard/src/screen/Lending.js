import Search from "../component/Search"
import {
    Flex,
    Stack,
    Box,
    Heading
} from "@chakra-ui/react"
import Kpi from "../component/Kpi"
import Chart from "../component/Chart"


const Lending = () => {
    return (
        <Flex align="center" justifyContent="center" flexDir="column" mt={40}>
           <Search />
           <Stack m={10} mt={5} direction={["column", "row"]} spacing="24px">
                <Kpi title="Total Minted Volume" />
                <Kpi title="Total Burned Volume" />
                <Kpi title="Total Unique User Minted" />
                <Kpi title="Total Unique User Burned" />
            </Stack>
            <Box w={1000} h={400} mb={10} flex="1" bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" align="center">
                <center>
                    <Heading as="h4" size="md" m={0} mb={5} mt={5}>
                         Total Volume Minted and Burned
                    </Heading>
                </center>
                <Chart />
            </Box>
            <Box w={1000} h={400} mb={10} flex="1" bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" align="center">
                <center>
                    <Heading as="h4" size="md" m={0} mb={5} mt={5}>
                         Total Unique User Minted and Burned
                    </Heading>
                </center>
                <Chart />
            </Box>
        </Flex>

    )
}

export default Lending