import './App.css';
import {
  ThemeProvider,
  theme,
  Flex,
  ButtonGroup,
  Button
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
        <Flex m={5} display="flex" align="center" justifyContent="center">
           <ButtonGroup size="sm" isAttached variant="outline">
                <Button colorScheme="teal" variant="solid"><Link to="/">Swap Analytics</Link></Button>
                <Button colorScheme="teal" variant="solid"><Link to="/lending">Lending Analytics</Link></Button>
                <Button colorScheme="teal" variant="solid"><Link to="/borrow">Borrowing Analytics</Link></Button>
            </ButtonGroup> 
        </Flex>

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
