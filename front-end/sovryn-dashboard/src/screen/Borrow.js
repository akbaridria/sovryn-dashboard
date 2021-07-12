import Search from "../component/Search"
import {
    Flex,
    Box,
    Heading,
    Stack,
    Alert,
    Badge,
    AlertTitle,
    AlertDescription,
    AlertIcon,
    Spinner
} from "@chakra-ui/react"
import Chart from "../component/Chart"
import Kpi from "../component/Kpi"
import React from "react"
import axios from "axios"


const Borrowing = () => {
    const [ borrowVolume, setBorrowVolume] = React.useState(0)
    const [ borrowUser, setBorrowUser] = React.useState(0)
    const [ borrowTransactions, setBorrowTransactions] = React.useState(0)
    const [ borrowVolumeDate, setBorrowVolumeDate] = React.useState([])
    const [ borrowUserDate, setBorrowUserDate ] = React.useState([])
    const [ isLoading, setIsloading] = React.useState(false)
    const [ blockBorrowing, setBlockBorrowing] = React.useState(0)
    React.useEffect(()  => {
        getDataBorrow();
    }, [])

    function searchDataBorrow(val1, val2) {
        let paramUrl = "?from_date=" + val1 + "&to_date=" + val2
        console.log(paramUrl)
        getDataBorrow(paramUrl)
    }

    async function getDataBorrow(paramFilter="") {
        setIsloading(true)
        const urlKpiBorrow = axios.get("https://api-sovryn.akbaridria.com/api/get_kpi_borrowing" + paramFilter)
        const urlBorrowVolume = axios.get("https://api-sovryn.akbaridria.com/api/get_total_borrow_date" + paramFilter)
        const urlBorrowUser = axios.get("https://api-sovryn.akbaridria.com/api/get_total_user_borrow" + paramFilter)
        const url_block_borrowing = axios.get("https://api-sovryn.akbaridria.com/api/getblock/borrowing")

        axios.all([urlKpiBorrow, urlBorrowVolume, urlBorrowUser, url_block_borrowing]).then((...responses) => {
            console.log(responses)
            const rawKpiBorrow = responses[0][0]
            const rawBorrowVolume = responses[0][1]
            const rawBorrowUser = responses[0][2]
            const block_borrowing = responses[0][3]
            setBlockBorrowing(block_borrowing.data.block)
            setBorrowVolumeDate(rawBorrowVolume.data)
            setBorrowUserDate(rawBorrowUser.data)
            rawKpiBorrow.data.borrow ? setBorrowVolume(rawKpiBorrow.data.borrow) : setBorrowVolume(0)
            setBorrowUser(rawKpiBorrow.data.user)
            setBorrowTransactions(rawKpiBorrow.data.transactions)
        })
        setIsloading(false)
    }
    return (
        <Flex align="center" justifyContent="center" flexDir="column" mt={40}>
            <Search searchData={searchDataBorrow} />
            <Alert status="success" width={1380} variant="left-accent">
            <AlertIcon />
            <Box flex="1">
                <AlertTitle>Only Cover</AlertTitle>
                <AlertDescription display="block">
                <Badge variant="solid" mr={2}>RBTC</Badge><Badge variant="solid" mr={2}>DoC</Badge>
                </AlertDescription>
            </Box>
                <AlertTitle>Latest Sync Block</AlertTitle>
                <AlertDescription display="block">
                <Badge variant="solid" mr={2}>{blockBorrowing}</Badge>
                </AlertDescription>   
            </Alert>
            
            {
                isLoading ? (
                    <Spinner
                        thickness="4px"
                        speed="0.65s"
                        emptyColor="gray.200"
                        color="teal.500"
                        size="xl"
                        m={20}
                    />
                ) : (
                    <>
                    <Stack m={10} mt={5} direction={["column", "row"]} spacing="24px">
                        <Kpi title="Total Borrow Volume" total={borrowVolume} symbol="$" />
                        <Kpi title="Total Unique User Borrow" total={borrowUser} symbol="" />
                        <Kpi title="Total Borrow Transactions" total={borrowTransactions} symbol="" />
                    </Stack>
                    <Box w={1000} h={400} mb={10} flex="1" bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" align="center">
                        <center>
                            <Heading as="h4" size="md" m={0} mb={5} mt={5}>
                                Total Volume Borrow By Date
                            </Heading>
                        </center>
                        <Chart data={borrowVolumeDate} />
                    </Box>
                    <Box w={1000} h={400} mb={10} flex="1" bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" align="center">
                        <center>
                            <Heading as="h4" size="md" m={0} mb={5} mt={5}>
                                Total Unique User Borrow By Date
                            </Heading>
                        </center>
                        <Chart data={borrowUserDate} />
                    </Box>
                    </>
                )
            }
            
        </Flex>

    )
}

export default Borrowing