import Search from "../component/Search"
import {
    Flex,
    Box,
    Heading,
    Stack
} from "@chakra-ui/react"
import Chart from "../component/Chart"
import Kpi from "../component/Kpi"

const Borrowing = () => {
    return (
        <Flex align="center" justifyContent="center" flexDir="column">
            <Search />
            <Stack m={10} mt={5} direction={["column", "row"]} spacing="24px">
                <Kpi />
                <Kpi />
                <Kpi />
            </Stack>
            <Box w={1000} h={400} mb={10} flex="1" bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" align="center">
                <center>
                    <Heading as="h4" size="md" m={0} mb={5} mt={5}>
                         Total Volume Borrow By Date
                    </Heading>
                </center>
                <Chart />
            </Box>
            <Box w={1000} h={400} mb={10} flex="1" bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" align="center">
                <center>
                    <Heading as="h4" size="md" m={0} mb={5} mt={5}>
                         Total Unique User Borrow By Date
                    </Heading>
                </center>
                <Chart />
            </Box>
        </Flex>

    )
}

export default Borrowing