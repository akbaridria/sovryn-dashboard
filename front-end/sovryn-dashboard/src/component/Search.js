import {
    Stack,
    Input,
    Button
} from "@chakra-ui/react"
import { Search2Icon } from '@chakra-ui/icons'
import React from "react"
import Swal from "sweetalert2"

const Search = ({searchData}) => {
    const [fromDate, setFromDate] = React.useState("")
    const [toDate, setToDate] = React.useState("")

    function sendData() {
        console.log("data")
        if(fromDate > toDate) {
            Swal.fire({  
                title: 'Not Allowed!',  
                text: 'From Date is Bigger than To Date',  
                icon: 'error',  
                confirmButtonText: 'Ok!'  
              });  
        } else {
            if(fromDate === "" || toDate ==="") {
                Swal.fire({  
                    title: 'Not Allowed!',  
                    text: 'Please filled from and to date!',  
                    icon: 'error',  
                    confirmButtonText: 'Ok!'  
                  });  
            } else {
                searchData(fromDate, toDate)
            }
            
        }
        
    }
    return (
        <Stack m={10} mt={5} direction={["column", "row"]} spacing="24px" align="center">
                <span>From</span>
                <Input variant="filled" type="date" value={fromDate} name="fromDate" onChange={(event) => setFromDate(event.target.value)} />
                <span>To</span>
                <Input variant="filled" type="date" value={toDate} name="toDate" onChange={(event) => setToDate(event.target.value)} />
                <Button colorScheme="teal" variant="solid" w={200} onClick={() => sendData()}>
                    <Search2Icon />
                </Button>
            </Stack>
    )
}

export default Search