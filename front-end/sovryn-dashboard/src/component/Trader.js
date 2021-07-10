import {
    Input,
    Flex,
    Box,
    useClipboard,
    Button,
    Badge,
    Heading,
    InputGroup,
    InputRightElement
} from "@chakra-ui/react"
import React, { useEffect } from "react";

const Trader = ({data}) => {

    const [value, setValue] = React.useState("")
    const { hasCopied, onCopy } = useClipboard(value)
    useEffect(() => {
        setValue(data.trader)
    })
    return (
        <Flex mb={3}>
            <Box bg="white" boxShadow="lg" rounded="md" border="1px" borderColor="gray.200" w={330} h={70} p={2}>
            <Flex mb={1}>
                <InputGroup size="md" alignItems="center">
                <Input
                    value={value} isReadOnly placeholder="Welcome" size="sm" pr="4.5rem" variant="filled"
                />
                <InputRightElement width="4.5rem">
                <Button onClick={onCopy} ml={2} size="xs">
                {hasCopied ? "Copied" : "Copy"}
                </Button>
                </InputRightElement>
                </InputGroup>                
            </Flex>
            <Flex flexDir="row" align="center" justifyContent="space-between">
            <Badge colorScheme="teal" variant="solid" >Total Trade Volume</Badge>
                <Heading fontSize="14" isTruncated>
                    $ {Number((data.volume).toFixed(2)).toLocaleString()}
                </Heading>
            </Flex>
            
            </Box>
            
        </Flex>
    )
}

export default Trader