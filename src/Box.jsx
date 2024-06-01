import { useFrame } from "@react-three/fiber";
import React from 'react'

export function Box() {
  
  const myMesh = React.useRef()
  useFrame(({ clock }) => {
    //const a = clock.getElapsedTime()
    //console.log(a) // the value will be 0 at scene initialization and grow each frame
    myMesh.current.rotation.x = clock.getElapsedTime()
    myMesh.current.rotation.y = clock.getElapsedTime()
  })
  return (
    <mesh ref={myMesh}>
      <boxGeometry />
      <meshBasicMaterial color="royalblue" />
    </mesh>
  )
}