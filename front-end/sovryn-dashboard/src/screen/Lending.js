import Search from "../component/Search"
import {
    Flex,
    Stack,
    Box,
    Heading,
    Alert,
    Badge,
    AlertTitle,
    AlertDescription,
    AlertIcon
} from "@chakra-ui/react"
import Kpi from "../component/Kpi"
import Chart from "../component/Chart"
import React from "react"
import axios from "axios"
import ChartTwoLine from "../component/ChartTwoLine"

const Lending = () => {

    const [totalMinted, setTotalMinted] = React.useState(0);
    const [totalBurned, setTotalBurned] = React.useState(0);
    const [totalUserMinted, setTotalUserMinted] = React.useState(0);
    const [totalUserBurned, setTotalUserBurned] = React.useState(0);
    const [mintBurnDateVolume, setMintBurnDateVolume] = React.useState([])
    const [mintBurnDateUser, setMintBurnDateUser] = React.useState([])

    async function getDataLending(paramFilter=""){
        const urlKpiLending = axios.get("https://api-sovryn.akbaridria.com/api/get_kpi_lending" + paramFilter)
        const urlMintBurnVolume = axios.get("https://api-sovryn.akbaridria.com/api/get_mint_burn" + paramFilter)
        const urlMintBurnUser = axios.get("https://api-sovryn.akbaridria.com/api/get_user_mint_burn" + paramFilter)
        await axios.all([urlKpiLending, urlMintBurnVolume, urlMintBurnUser]).then((...responses) => {
            const rawKPI = responses[0][0]
            const rawMintBurnVol = responses[0][1]
            const rawMintBurnUs = responses[0][2]
            console.log(responses)
            setTotalMinted(rawKPI.data[1].total)
            setTotalBurned(rawKPI.data[0].total)
            setTotalUserBurned(rawKPI.data[0].user)
            setTotalUserMinted(rawKPI.data[1].user)
            setMintBurnDateVolume(rawMintBurnVol.data)
            setMintBurnDateUser(rawMintBurnUs.data)
        })
        
    }

    React.useEffect(() => {
        getDataLending();
    }, [])

    return (
        <Flex align="center" justifyContent="center" flexDir="column" mt={40}>
           <Search />
           <Alert status="success" width={1380} variant="left-accent">
            <AlertIcon />
            <Box flex="1">
                <AlertTitle>Only Cover</AlertTitle>
                <AlertDescription display="block">
                <Badge variant="solid" mr={2}>iUSDT</Badge><Badge variant="solid" mr={2}>iRBTC</Badge><Badge variant="solid" mr={2}>iSUSD</Badge><Badge variant="solid" mr={2}>iXUSD</Badge>
                </AlertDescription>
            </Box>
                <AlertTitle>Latest Sync Block</AlertTitle>
                <AlertDescription display="block">
                <Badge variant="solid" mr={2}>3141234123</Badge>
                </AlertDescription>   
            </Alert>
           <Stack m={10} mt={5} direction={["column", "row"]} spacing="24px">
                <Kpi title="Total Minted Volume" total={totalMinted} symbol="$" />
                <Kpi title="Total Burned Volume" total={totalBurned} symbol="$" />
                <Kpi title="Total Unique User Minted" total={totalUserMinted} symbol="" />
                <Kpi title="Total Unique User Burned" total={totalUserBurned} symbol="" />
            </Stack>
            <Box w={1000} h={400} mb={10} flex="1" bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" align="center">
                <center>
                    <Heading as="h4" size="md" m={0} mb={5} mt={5}>
                         Total Volume Minted and Burned
                    </Heading>
                </center>
                <ChartTwoLine data={mintBurnDateVolume} />
            </Box>
            <Box w={1000} h={400} mb={10} flex="1" bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" align="center">
                <center>
                    <Heading as="h4" size="md" m={0} mb={5} mt={5}>
                         Total Unique User Minted and Burned
                    </Heading>
                </center>
                <ChartTwoLine data={mintBurnDateUser} />
            </Box>
        </Flex>

    )
}

export default Lending