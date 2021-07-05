import {
    Stack,
    Flex,
    Select,
    Input,
    Button,
    Box,
    Heading
} from "@chakra-ui/react"
import { Search2Icon } from '@chakra-ui/icons'
import Kpi from "../component/Kpi";
import Pie from "../component/PoolDistribution";
import Chart from "../component/Chart";


const Swap = () => {
    return (
        <Flex align="center" justifyContent="center" flexDir="column">
            <Stack m={10} mt={5} direction={["column", "row"]} spacing="24px" align="center">
                <span>From</span>
                <Input variant="filled" type="date"/>
                <span>To</span>
                <Input variant="filled" type="date" />
                <Input variant="filled" placeholder="Wallet Address" />
                <Select variant="filled" placeholder="Pool" size="md">
                    <option>asd</option>
                    <option>asd</option>
                    <option>asd</option>
                </Select>
                <Button colorScheme="teal" variant="solid" w={200}>
                    <Search2Icon />
                </Button>
            </Stack>
            <Stack m={10} mt={5} direction={["column", "row"]} spacing="24px">
                <Kpi />
                <Kpi />
                <Kpi />
                <Kpi />
            </Stack>
            <Stack m={10} mt={5} direction={["column", "row"]} spacing="24px">
                <Box w={400} h={300} boxShadow="lg" rounded="md" bg="white" border="1px" borderColor="gray.200" align="center">
                    <center>
                    <Heading as="h4" size="md" m={0} mt={5}>
                        Pool Distribution By Volume
                    </Heading>
                    </center>
                    <Pie />
                </Box>
                <Box w={1000} h={300} flex="1" bg="tomato" boxShadow="lg" rounded="md" bg="white" border="1px" borderColor="gray.200" align="center">
                    <center>
                    <Heading as="h4" size="md" m={0} mb={5} mt={5}>
                        Total Swap By Date
                    </Heading>
                    </center>
                    <Chart />
                </Box>
            </Stack>
        </Flex>
        
    )
}

export default Swap;