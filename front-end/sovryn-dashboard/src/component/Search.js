import {
    Stack,
    Input,
    Button
} from "@chakra-ui/react"
import { Search2Icon } from '@chakra-ui/icons'


const Search = () => {
    return (
        <Stack m={10} mt={5} direction={["column", "row"]} spacing="24px" align="center">
                <span>From</span>
                <Input variant="filled" type="date"/>
                <span>To</span>
                <Input variant="filled" type="date" />
                <Input variant="filled" placeholder="Wallet Address" />
                <Button colorScheme="teal" variant="solid" w={200}>
                    <Search2Icon />
                </Button>
            </Stack>
    )
}

export default Search