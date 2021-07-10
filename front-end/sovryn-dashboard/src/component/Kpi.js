import {
    Box,
    Heading
} from "@chakra-ui/react"

const Kpi = ({title, total, symbol}) => {
    return (
        <Box width={300} height={75} border="1px" borderColor="gray.200" p={3} boxShadow="lg" rounded="md" bg="white" >
            <center>
               <Heading as="h4" size="md" m={0}>
                    {title}
                </Heading>
                <Heading as="h3" size="lg" m={0} mt={3} color="teal">
                    {symbol + Number((total).toFixed(0)).toLocaleString()}
                </Heading>
            </center>
        </Box>
    )
}


export default Kpi