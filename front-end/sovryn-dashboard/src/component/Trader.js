import {
    Input,
    Flex,
    Box,
    useClipboard,
    Button,
    Badge,
    Heading
} from "@chakra-ui/react"
import React from "react";

const Trader = () => {

    const [value, setValue] = React.useState("0xf36c7f8706fD618BD280cE706b327C268be2f368")
    const { hasCopied, onCopy } = useClipboard(value)

    return (
        <Flex m={3}>
            <Box bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" w={330} h={100} p={2}>
            <Flex mb={2}>
                <Input value={value} isReadOnly placeholder="Welcome" size="sm"/>
                <Button onClick={onCopy} ml={2} size="sm">
                {hasCopied ? "Copied" : "Copy"}
                </Button>
            </Flex>
            <Badge colorScheme="teal" >Total Trade Volume</Badge>
            <Flex flexDir="column">
                
                <Heading fontSize="14" isTruncated>
                    $ 100.000.000,00
                </Heading>
            </Flex>
            
            </Box>
            
        </Flex>
    )
}

export default Trader