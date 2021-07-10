import './App.css';
import {
  ThemeProvider,
  theme,
  Flex,
  ButtonGroup,
  Button,
  Box
} from "@chakra-ui/react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Swap from './screen/Swap';
import Lending from './screen/Lending';
import Borrowing from './screen/Borrow';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Router>
        <Box position="fixed" top={0} width="100%" boxShadow="lg" p="6" rounded="md" bg="white" zIndex={9}>
        <Flex display="flex" align="center" flexDir="column" justifyContent="center" >
           <ButtonGroup size="sm" isAttached variant="outline">
                <Button colorScheme="teal" variant="solid"><Link to="/">Swap Analytics</Link></Button>
                <Button colorScheme="teal" variant="solid"><Link to="/lending">Lending Analytics</Link></Button>
                <Button colorScheme="teal" variant="solid"><Link to="/borrow">Borrowing Analytics</Link></Button>
            </ButtonGroup>
        </Flex>
        </Box>
        

        <Switch>
          <Route exact path="/">
            <SwapScreen />
          </Route>
          <Route path="/lending">
            <LendingScreen />
          </Route>
          <Route path="/borrow">
            <BorrowScreen />
          </Route>
        </Switch>
      </Router>
        
    </ThemeProvider>
  );
}

function SwapScreen() {
  return (
    <>
      <Swap />
    </>
  );
}

function LendingScreen() {
  return (
    <>
      <Lending />
    </>
  );
}

function BorrowScreen() {
  return (
    <>
     <Borrowing />
    </>
  );
}

export default App;
