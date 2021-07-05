import {
    Box,
    Heading
} from "@chakra-ui/react"

const Kpi = () => {
    return (
        <Box width={300} height={75} border="1px" borderColor="gray.200" p={3} boxShadow="lg" rounded="md" bg="white" >
            <center>
               <Heading as="h4" size="md" m={0}>
                    The Largest Swap
                </Heading>
                <Heading as="h3" size="lg" m={0} mt={3} color="teal">
                    $ 10,000,000.00
                </Heading>
            </center>
        </Box>
    )
}


export default Kpi