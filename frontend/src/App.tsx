import { Home } from '@/pages/Home'
import { Route, Routes } from 'react-router-dom'

export default function App(): JSX.Element {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
    </Routes>
  )
}
